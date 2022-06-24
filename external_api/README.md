# OdooAPI

OdooAPI is a wrapper for Odoo XMLRPC external API. It has been developed to 
reduce syntax use redundancy for some operations as well as to extend some 
operations for business specific application.



## Prerequisite
OdooAPI has been simplified after analysing different use cases. However, 
it is recommended to read [official Odoo XMLRPC External API](https://www.odoo.com/documentation/15.0/developer/misc/api/external_api.html) to fully understand
interfacing technique with Odoo. Here, you need following information to use OdooAPI -

- Odoo user email
- API access_token
- database name
- Server URL

## Technical Details

We tested this module with `python3.7`, `python3.8` and `python3.10`. Since no third party libray
has been used, it supports all versions of python 3

## Getting Started

- Clone this repo and access to the directory

```
https://github.com/mahbubrman/odoo_technical_training_exercise.git
cd external_api
```

- Open a python file or Notebook and setup the `odoo` client

```python
from rpc import OdooAPI

odoo = OdooAPI(
    server="https://HOST_or_IP",
    database_name="Odoo_DATABASE_NAME",
    username="Odoo_USER_EMAIL",
    access_token="USER_ACCESS_TOKEN"
)
```

## Example Use

Read a record

```python
# Get user details of id 3
user_records = odoo.read('res.partner', [3])

# Get user specific(name, country_id) details 
user_spec = odoo.read('res.partner', [3], ['name', 'country_id'])
```

OdooApi has all sorts of operations such as, `search`, `read`, `search_read`, `get_fields`, `create`, `update` and 
`delete`. Odoo XMLRPC has its alternative names for `get_fields`, `update` and
`delete`. They are called, `fields_get`, `write`, `unlink` respectively. 