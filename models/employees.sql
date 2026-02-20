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
    end as salary_category
from {{ ref('raw_employees') }}
