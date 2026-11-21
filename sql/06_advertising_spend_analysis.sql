
-- =====================================================
-- 06. ADVERTISING SPEND & CONVERSION ANALYSIS
-- =====================================================

-- 1. Average Advertising Spend by Conversion Status
SELECT
    conversion,
    COUNT(*) AS total_customers,
    ROUND(AVG(adspend), 2) AS average_ad_spend,
    ROUND(SUM(adspend), 2) AS total_ad_spend
FROM marketing_campaigns
GROUP BY conversion
ORDER BY conversion;


-- 2. Conversion Performance by Advertising Spend Group
SELECT
    CASE
        WHEN adspend < 2500 THEN 'Low Spend'
        WHEN adspend < 5000 THEN 'Medium Spend'
        WHEN adspend < 7500 THEN 'High Spend'
        ELSE 'Very High Spend'
    END AS ad_spend_group,
    COUNT(*) AS total_customers,
    SUM(conversion) AS converted_customers,
    ROUND(
        SUM(conversion)::NUMERIC / COUNT(*) * 100,
        2
    ) AS conversion_rate_percentage,
    ROUND(AVG(adspend), 2) AS average_ad_spend
FROM marketing_campaigns
GROUP BY ad_spend_group
ORDER BY MIN(adspend);


-- 3. Conversion Performance by Click Through Rate
SELECT
    CASE
        WHEN clickthroughrate < 0.10 THEN 'Low CTR'
        WHEN clickthroughrate < 0.20 THEN 'Medium CTR'
        WHEN clickthroughrate < 0.30 THEN 'High CTR'
        ELSE 'Very High CTR'
    END AS ctr_group,
    COUNT(*) AS total_customers,
    SUM(conversion) AS converted_customers,
    ROUND(
        SUM(conversion)::NUMERIC / COUNT(*) * 100,
        2
    ) AS conversion_rate_percentage,
    ROUND(AVG(clickthroughrate) * 100, 2) AS average_ctr_percentage
FROM marketing_campaigns
GROUP BY ctr_group
ORDER BY MIN(clickthroughrate);


-- 4. Conversion Performance by Conversion Rate Metric
SELECT
    CASE
        WHEN conversionrate < 0.05 THEN 'Below 5%'
        WHEN conversionrate < 0.10 THEN '5-10%'
        WHEN conversionrate < 0.15 THEN '10-15%'
        ELSE '15% and Above'
    END AS conversion_rate_group,
    COUNT(*) AS total_customers,
    SUM(conversion) AS converted_customers,
    ROUND(
        SUM(conversion)::NUMERIC / COUNT(*) * 100,
        2
    ) AS actual_conversion_percentage,
    ROUND(AVG(conversionrate) * 100, 2) AS average_conversion_rate_metric
FROM marketing_campaigns
GROUP BY conversion_rate_group
ORDER BY MIN(conversionrate);


-- 5. Advertising Spend and Customer Engagement
SELECT
    CASE
        WHEN adspend < 2500 THEN 'Low Spend'
        WHEN adspend < 5000 THEN 'Medium Spend'
        WHEN adspend < 7500 THEN 'High Spend'
        ELSE 'Very High Spend'
    END AS ad_spend_group,
    COUNT(*) AS total_customers,
    ROUND(AVG(clickthroughrate) * 100, 2) AS average_ctr_percentage,
    ROUND(AVG(websitevisits), 2) AS avg_website_visits,
    ROUND(AVG(timeonsite), 2) AS avg_time_on_site,
    ROUND(AVG(conversion), 4) AS average_conversion
FROM marketing_campaigns
GROUP BY ad_spend_group
ORDER BY MIN(adspend);


-- 6. Overall Correlation Between Advertising Metrics and Conversion
SELECT
    ROUND(CORR(adspend, conversion::NUMERIC)::NUMERIC, 4)
        AS ad_spend_conversion_correlation,
    ROUND(CORR(clickthroughrate, conversion::NUMERIC)::NUMERIC, 4)
        AS ctr_conversion_correlation,
    ROUND(CORR(conversionrate, conversion::NUMERIC)::NUMERIC, 4)
        AS conversionrate_conversion_correlation
FROM marketing_campaigns;
