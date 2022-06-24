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

## Example Use and Comparison

Let's compare a simple  read operation syntax between original xmlrpc client and OdooAPI client.  Let's call XMLRPC client as client here and OdooAPI client is odoo as we initialised in above section.



For XMLRPC client it looks like this where you want to know a name for a user_id=11

```python
record = client.execute_kw("DATABASE_NAME", "USER_ID", "ACCESS_TOKEN",
'res.partner', 'read', [[11]], {'fields': 'name'})
```

In case of OdooAPI client

```python
record = odoo.read('res.partner', [11], ['name'])
```


Another example here for updating a record in a model
```python
client.update("DATABASE_NAME", "USER_ID", "ACCESS_TOKEN",
'res.parter', 'write', [[11],
{'name': 'Mahbubur Rahman', 'country_code': 'BD'} )
```

Exact same operation can be performed with minimal code in OdooAPI client

```python
odoo.update('res.parter', [11], name='Mahbubur Rahman', country_code='BD')
```

It reduces code!


OdooApi has all sorts of operations such as, `search`, `read`, `search_read`, `get_fields`, `create`, `update` and 
`delete`. Odoo XMLRPC has its alternative names for `get_fields`, `update` and
`delete`. They are called, `fields_get`, `write`, `unlink` respectively. 