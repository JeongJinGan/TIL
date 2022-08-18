Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@JeongJinGan 
kdt-hphk
/
01-resources
Public
Code
Issues
Pull requests
1
Actions
Projects
Security
Insights
01-resources/db/06_function.sql
@kdt-live
kdt-live 0818 DB
Latest commit 3c8bc71 11 minutes ago
 History
 1 contributor
64 lines (56 sloc)  1.29 KB

SELECT * FROM users LIMIT 1;

-- pipe sign 엔터 위에 있어요 보통
-- 문자열 합치기 ||
-- (성+이름) 출력, 5명만
SELECT 
    last_name || first_name 이름,
    age,
    country,
    phone,
    balance
FROM users
LIMIT 5;

-- 이름   age  country  phone          balance
-- ---  ---  -------  -------------  -------
-- 유정호  40   전라북도     016-7280-2855  370
-- 이경희  36   경상남도     011-9854-5133  5900
-- 구정자  37   전라남도     011-4177-8170  3100
-- 장미경  40   충청남도     011-9079-4419  250000
-- 차영환  30   충청북도     011-2921-4284  220

-- 문자열 길이 LENGTH
SELECT 
    LENGTH(first_name),
    first_name
FROM users
LIMIT 5;
-- LENGTH(first_name)  first_name
-- ------------------  ----------
-- 2                   정호
-- 2                   경희
-- 2                   정자
-- 2                   미경
-- 2                   영환

-- 문자열 변경 REPLACE
-- 016-7280-2855 => 01672802855
SELECT 
    first_name,
    phone,
    REPLACE(phone, '-', '')
FROM users
LIMIT 5;

-- 숫자 활용
SELECT MOD(5, 2)
FROM users
LIMIT 1;

-- 올림, 내림, 반올림
SELECT CEIL(3.14), FLOOR(3.14), ROUND(3.14)
FROM users
LIMIT 1;

-- 9의 제곱근
SELECT SQRT(9)
FROM users
LIMIT 1;

-- 9^2
SELECT POWER(9, 2)
FROM users
LIMIT 1;
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
You have no unread notifications