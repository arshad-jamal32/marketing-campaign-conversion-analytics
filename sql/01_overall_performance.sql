
-- =====================================================
-- MARKETING CAMPAIGN & CUSTOMER CONVERSION ANALYTICS
-- 01. OVERALL PERFORMANCE ANALYSIS
-- =====================================================

-- 1. Total Customers
SELECT
    COUNT(*) AS total_customers
FROM marketing_campaigns;


-- 2. Total Converted and Non-Converted Customers
SELECT
    conversion,
    COUNT(*) AS total_customers
FROM marketing_campaigns
GROUP BY conversion
ORDER BY conversion;


-- 3. Overall Conversion Rate
SELECT
    COUNT(*) AS total_customers,
    SUM(conversion) AS converted_customers,
    COUNT(*) - SUM(conversion) AS non_converted_customers,
    ROUND(
        SUM(conversion)::NUMERIC / COUNT(*) * 100,
        2
    ) AS conversion_rate_percentage
FROM marketing_campaigns;


-- 4. Average Customer and Campaign Metrics
SELECT
    ROUND(AVG(age), 2) AS average_age,
    ROUND(AVG(income), 2) AS average_income,
    ROUND(AVG(adspend), 2) AS average_ad_spend,
    ROUND(AVG(websitevisits), 2) AS average_website_visits,
    ROUND(AVG(timeonsite), 2) AS average_time_on_site,
    ROUND(AVG(emailopens), 2) AS average_email_opens,
    ROUND(AVG(emailclicks), 2) AS average_email_clicks
FROM marketing_campaigns;


-- 5. Overall Marketing Spend
SELECT
    ROUND(SUM(adspend), 2) AS total_advertising_spend,
    ROUND(AVG(adspend), 2) AS average_advertising_spend
FROM marketing_campaigns;
