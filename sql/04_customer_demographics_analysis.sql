
-- =====================================================
-- 04. CUSTOMER DEMOGRAPHICS ANALYSIS
-- =====================================================

-- 1. Customer Distribution by Gender
SELECT
    gender,
    COUNT(*) AS total_customers
FROM marketing_campaigns
GROUP BY gender
ORDER BY total_customers DESC;


-- 2. Conversion Performance by Gender
SELECT
    gender,
    COUNT(*) AS total_customers,
    SUM(conversion) AS converted_customers,
    ROUND(
        SUM(conversion)::NUMERIC / COUNT(*) * 100,
        2
    ) AS conversion_rate_percentage
FROM marketing_campaigns
GROUP BY gender
ORDER BY conversion_rate_percentage DESC;


-- 3. Customer Distribution by Age Group
SELECT
    CASE
        WHEN age < 25 THEN '18-24'
        WHEN age < 35 THEN '25-34'
        WHEN age < 45 THEN '35-44'
        WHEN age < 55 THEN '45-54'
        WHEN age < 65 THEN '55-64'
        ELSE '65+'
    END AS age_group,
    COUNT(*) AS total_customers
FROM marketing_campaigns
GROUP BY age_group
ORDER BY MIN(age);


-- 4. Conversion Performance by Age Group
SELECT
    CASE
        WHEN age < 25 THEN '18-24'
        WHEN age < 35 THEN '25-34'
        WHEN age < 45 THEN '35-44'
        WHEN age < 55 THEN '45-54'
        WHEN age < 65 THEN '55-64'
        ELSE '65+'
    END AS age_group,
    COUNT(*) AS total_customers,
    SUM(conversion) AS converted_customers,
    ROUND(
        SUM(conversion)::NUMERIC / COUNT(*) * 100,
        2
    ) AS conversion_rate_percentage
FROM marketing_campaigns
GROUP BY age_group
ORDER BY MIN(age);


-- 5. Conversion Performance by Income Group
SELECT
    CASE
        WHEN income < 40000 THEN 'Low Income'
        WHEN income < 80000 THEN 'Lower-Middle Income'
        WHEN income < 120000 THEN 'Upper-Middle Income'
        ELSE 'High Income'
    END AS income_group,
    COUNT(*) AS total_customers,
    SUM(conversion) AS converted_customers,
    ROUND(
        SUM(conversion)::NUMERIC / COUNT(*) * 100,
        2
    ) AS conversion_rate_percentage,
    ROUND(AVG(income), 2) AS average_income
FROM marketing_campaigns
GROUP BY income_group
ORDER BY MIN(income);


-- 6. Average Income by Conversion Status
SELECT
    conversion,
    COUNT(*) AS total_customers,
    ROUND(AVG(income), 2) AS average_income,
    ROUND(AVG(age), 2) AS average_age
FROM marketing_campaigns
GROUP BY conversion
ORDER BY conversion;
