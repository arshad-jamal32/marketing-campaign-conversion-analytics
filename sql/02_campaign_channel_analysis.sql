
-- =====================================================
-- 02. CAMPAIGN CHANNEL PERFORMANCE ANALYSIS
-- =====================================================

-- 1. Customer Distribution by Campaign Channel
SELECT
    campaignchannel,
    COUNT(*) AS total_customers
FROM marketing_campaigns
GROUP BY campaignchannel
ORDER BY total_customers DESC;


-- 2. Conversion Performance by Campaign Channel
SELECT
    campaignchannel,
    COUNT(*) AS total_customers,
    SUM(conversion) AS converted_customers,
    COUNT(*) - SUM(conversion) AS non_converted_customers,
    ROUND(
        SUM(conversion)::NUMERIC / COUNT(*) * 100,
        2
    ) AS conversion_rate_percentage
FROM marketing_campaigns
GROUP BY campaignchannel
ORDER BY conversion_rate_percentage DESC;


-- 3. Advertising Spend by Campaign Channel
SELECT
    campaignchannel,
    ROUND(SUM(adspend), 2) AS total_ad_spend,
    ROUND(AVG(adspend), 2) AS average_ad_spend
FROM marketing_campaigns
GROUP BY campaignchannel
ORDER BY total_ad_spend DESC;


-- 4. Customer Engagement by Campaign Channel
SELECT
    campaignchannel,
    ROUND(AVG(websitevisits), 2) AS avg_website_visits,
    ROUND(AVG(timeonsite), 2) AS avg_time_on_site,
    ROUND(AVG(emailopens), 2) AS avg_email_opens,
    ROUND(AVG(emailclicks), 2) AS avg_email_clicks
FROM marketing_campaigns
GROUP BY campaignchannel
ORDER BY avg_time_on_site DESC;


-- 5. Channel-wise Conversion and Advertising Spend
SELECT
    campaignchannel,
    COUNT(*) AS total_customers,
    ROUND(SUM(adspend), 2) AS total_ad_spend,
    SUM(conversion) AS converted_customers,
    ROUND(
        SUM(adspend) / NULLIF(SUM(conversion), 0),
        2
    ) AS ad_spend_per_converted_customer
FROM marketing_campaigns
GROUP BY campaignchannel
ORDER BY ad_spend_per_converted_customer ASC;
