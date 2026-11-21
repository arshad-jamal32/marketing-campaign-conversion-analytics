
-- =====================================================
-- 07. ADVANCED SQL ANALYSIS
-- =====================================================


-- 1. Rank Campaign Channels by Conversion Rate (CTE + RANK)

WITH channel_performance AS (
    SELECT
        campaignchannel,
        COUNT(*) AS total_customers,
        SUM(conversion) AS converted_customers,
        ROUND(
            SUM(conversion)::NUMERIC / COUNT(*) * 100,
            2
        ) AS conversion_rate
    FROM marketing_campaigns
    GROUP BY campaignchannel
)

SELECT
    campaignchannel,
    total_customers,
    converted_customers,
    conversion_rate,
    RANK() OVER (
        ORDER BY conversion_rate DESC
    ) AS channel_rank
FROM channel_performance;


-- 2. Rank Campaign Types by Advertising Efficiency (CTE + DENSE_RANK)

WITH campaign_performance AS (
    SELECT
        campaigntype,
        COUNT(*) AS total_customers,
        SUM(conversion) AS converted_customers,
        ROUND(SUM(adspend), 2) AS total_ad_spend,
        ROUND(
            SUM(adspend) / NULLIF(SUM(conversion), 0),
            2
        ) AS spend_per_conversion
    FROM marketing_campaigns
    GROUP BY campaigntype
)

SELECT
    campaigntype,
    total_customers,
    converted_customers,
    total_ad_spend,
    spend_per_conversion,
    DENSE_RANK() OVER (
        ORDER BY spend_per_conversion ASC
    ) AS efficiency_rank
FROM campaign_performance;


-- 3. Top 3 Highest-Spending Customers in Each Channel
-- (ROW_NUMBER + PARTITION BY)

WITH ranked_customers AS (
    SELECT
        customerid,
        campaignchannel,
        adspend,
        conversion,
        ROW_NUMBER() OVER (
            PARTITION BY campaignchannel
            ORDER BY adspend DESC
        ) AS customer_rank
    FROM marketing_campaigns
)

SELECT
    customerid,
    campaignchannel,
    adspend,
    conversion,
    customer_rank
FROM ranked_customers
WHERE customer_rank <= 3
ORDER BY campaignchannel, customer_rank;


-- 4. Customer Segmentation by Advertising Spend
-- (NTILE Window Function)

WITH spend_segments AS (
    SELECT
        customerid,
        adspend,
        conversion,
        NTILE(4) OVER (
            ORDER BY adspend
        ) AS spend_quartile
    FROM marketing_campaigns
)

SELECT
    spend_quartile,
    COUNT(*) AS total_customers,
    ROUND(AVG(adspend), 2) AS average_ad_spend,
    SUM(conversion) AS converted_customers,
    ROUND(
        AVG(conversion::NUMERIC) * 100,
        2
    ) AS conversion_rate_percentage
FROM spend_segments
GROUP BY spend_quartile
ORDER BY spend_quartile;


-- 5. Compare Individual Customer Spend with Channel Average
-- (AVG + PARTITION BY)

SELECT
    customerid,
    campaignchannel,
    ROUND(adspend, 2) AS customer_ad_spend,
    ROUND(
        AVG(adspend) OVER (
            PARTITION BY campaignchannel
        ),
        2
    ) AS channel_average_ad_spend,
    ROUND(
        adspend - AVG(adspend) OVER (
            PARTITION BY campaignchannel
        ),
        2
    ) AS difference_from_channel_average
FROM marketing_campaigns
ORDER BY campaignchannel, customerid
LIMIT 20;


-- 6. Rank Customer Engagement Within Each Campaign Type
-- (RANK + PARTITION BY)


-- Top 5 Most Engaged Customers in Each Campaign Type

WITH customer_engagement AS (
    SELECT
        customerid,
        campaigntype,
        websitevisits,
        timeonsite,
        emailclicks,
        (
            websitevisits +
            timeonsite +
            emailclicks
        ) AS engagement_score
    FROM marketing_campaigns
),

ranked_customers AS (
    SELECT
        *,
        RANK() OVER (
            PARTITION BY campaigntype
            ORDER BY engagement_score DESC
        ) AS engagement_rank
    FROM customer_engagement
)

SELECT
    customerid,
    campaigntype,
    websitevisits,
    timeonsite,
    emailclicks,
    engagement_score,
    engagement_rank
FROM ranked_customers
WHERE engagement_rank <= 5
ORDER BY campaigntype, engagement_rank;
