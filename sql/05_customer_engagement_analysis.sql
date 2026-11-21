
-- =====================================================
-- 05. CUSTOMER ENGAGEMENT ANALYSIS
-- =====================================================

-- 1. Average Engagement Metrics by Conversion Status
SELECT
    conversion,
    COUNT(*) AS total_customers,
    ROUND(AVG(websitevisits), 2) AS avg_website_visits,
    ROUND(AVG(pagespervisit), 2) AS avg_pages_per_visit,
    ROUND(AVG(timeonsite), 2) AS avg_time_on_site,
    ROUND(AVG(emailopens), 2) AS avg_email_opens,
    ROUND(AVG(emailclicks), 2) AS avg_email_clicks
FROM marketing_campaigns
GROUP BY conversion
ORDER BY conversion;


-- 2. Conversion Performance by Website Visits
SELECT
    CASE
        WHEN websitevisits < 10 THEN 'Low Visits'
        WHEN websitevisits < 20 THEN 'Medium Visits'
        WHEN websitevisits < 30 THEN 'High Visits'
        ELSE 'Very High Visits'
    END AS website_visit_group,
    COUNT(*) AS total_customers,
    SUM(conversion) AS converted_customers,
    ROUND(
        SUM(conversion)::NUMERIC / COUNT(*) * 100,
        2
    ) AS conversion_rate_percentage
FROM marketing_campaigns
GROUP BY website_visit_group
ORDER BY MIN(websitevisits);


-- 3. Conversion Performance by Time Spent on Website
SELECT
    CASE
        WHEN timeonsite < 5 THEN 'Below 5'
        WHEN timeonsite < 10 THEN '5-10'
        WHEN timeonsite < 15 THEN '10-15'
        ELSE '15 and Above'
    END AS time_spent_group,
    COUNT(*) AS total_customers,
    SUM(conversion) AS converted_customers,
    ROUND(
        SUM(conversion)::NUMERIC / COUNT(*) * 100,
        2
    ) AS conversion_rate_percentage
FROM marketing_campaigns
GROUP BY time_spent_group
ORDER BY MIN(timeonsite);


-- 4. Conversion Performance by Email Engagement
SELECT
    CASE
        WHEN emailclicks = 0 THEN 'No Clicks'
        WHEN emailclicks <= 3 THEN '1-3 Clicks'
        WHEN emailclicks <= 6 THEN '4-6 Clicks'
        ELSE '7+ Clicks'
    END AS email_click_group,
    COUNT(*) AS total_customers,
    SUM(conversion) AS converted_customers,
    ROUND(
        SUM(conversion)::NUMERIC / COUNT(*) * 100,
        2
    ) AS conversion_rate_percentage,
    ROUND(AVG(emailopens), 2) AS avg_email_opens
FROM marketing_campaigns
GROUP BY email_click_group
ORDER BY MIN(emailclicks);


-- 5. Conversion Performance by Previous Purchases
SELECT
    CASE
        WHEN previouspurchases = 0 THEN 'No Previous Purchases'
        WHEN previouspurchases <= 3 THEN '1-3 Purchases'
        WHEN previouspurchases <= 6 THEN '4-6 Purchases'
        ELSE '7+ Purchases'
    END AS purchase_group,
    COUNT(*) AS total_customers,
    SUM(conversion) AS converted_customers,
    ROUND(
        SUM(conversion)::NUMERIC / COUNT(*) * 100,
        2
    ) AS conversion_rate_percentage
FROM marketing_campaigns
GROUP BY purchase_group
ORDER BY MIN(previouspurchases);


-- 6. Conversion Performance by Loyalty Points
SELECT
    CASE
        WHEN loyaltypoints < 1000 THEN 'Below 1000'
        WHEN loyaltypoints < 2000 THEN '1000-1999'
        WHEN loyaltypoints < 3000 THEN '2000-2999'
        WHEN loyaltypoints < 4000 THEN '3000-3999'
        ELSE '4000+'
    END AS loyalty_points_group,
    COUNT(*) AS total_customers,
    SUM(conversion) AS converted_customers,
    ROUND(
        SUM(conversion)::NUMERIC / COUNT(*) * 100,
        2
    ) AS conversion_rate_percentage
FROM marketing_campaigns
GROUP BY loyalty_points_group
ORDER BY MIN(loyaltypoints);
