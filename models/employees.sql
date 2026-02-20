select 
    id,
    name,
    age,
    city,
    salary,
    case 
        when salary >= 80000 then 'High'
        when salary >= 60000 then 'Medium'
        else 'Low'
    end as salary_category,
    case 
        when age >= 40 then 'Senior'
        when age >= 30 then 'Mid'
        else 'Junior'
    end as age_group
from {{ ref('raw_employees') }}
