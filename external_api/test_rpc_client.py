from rpc import OdooAPI
import pytest
from dotenv import dotenv_values


from xmlrpc import client
credentials = dotenv_values('.env')
test_email = credentials["username"]

odoo = OdooAPI(**credentials)

cli = client.ServerProxy(f'{odoo.server}/xmlrpc/2/object')


@pytest.mark.parametrize('username, user_id', [(test_email, 11), ("altaf", False)])
def test_test(username: str, user_id: int):
    assert odoo.get_user_id(username) == user_id
    assert odoo.uid == 11


@pytest.mark.parametrize('ids', [([26])])
def test_read(ids: list):
    user_records = odoo.read('res.partner', ids, ['name', 'country_id'])
    org_userrec = cli.execute_kw(odoo.db, odoo.uid, odoo.access_token, 'res.partner',
                                 'read', [ids], {'fields': ['name', 'country_id']})

    assert user_records == org_userrec


@pytest.mark.parametrize('country_id, limit', [(False, 10)])
def test_search(country_id: int, limit: int):
    test_ids = odoo.search('res.partner', ['country_id', '=', country_id], {'limit': limit})
    org_testid = cli.execute_kw(odoo.db, odoo.uid, odoo.access_token, 'res.partner',
                                'search', [[['country_id', '=', country_id]]], {'limit': limit})

    assert test_ids == org_testid


@pytest.mark.parametrize('id', [(100)])
def test_search_read(id: int):
    user_rec = odoo.search_read('sale.order', ['id', '>', id], ['id'], limit=2)
    ids = []
    for user in user_rec:
        ids.append(user['id'])
    org_userrec = cli.execute_kw(odoo.db, odoo.uid, odoo.access_token, 'sale.order',
                                 'search_read', [[['id', '>', id]]],
                                 {'fields': ['id'], 'limit': 2})

    assert min(ids) > 100
    assert user_rec == org_userrec


@pytest.mark.parametrize('model', [('sale.order')])
def test_get_fields(model: str):
    fields = odoo.get_fields(model, ['name'], ['string'])
    org_fields = cli.execute_kw(odoo.db, odoo.uid, odoo.access_token, model,
                                'fields_get', ['name'], {'attributes': ['string']})

    assert fields == org_fields


@pytest.mark.parametrize('model, name', [('res.partner', 'finaltest')])
def test_create(model: str, name: str):
    test_id = odoo.create(model, [{'name': name}])

    assert odoo.search(model, ['name', '=', name])[0] == test_id


@pytest.mark.parametrize('model', [('res.partner')])  # id from created partner
def test_update(model: str):
    id = odoo.search(model, ['name', '=', 'finaltest'])
    updated = odoo.update(model, id, name='Final Toast')

    assert updated == True


@pytest.mark.parametrize('model', [('res.partner')])  # id from created partner
def test_delete(model: str):
    id = odoo.search(model, ['name', '=', 'Final Toast'])
    deleted = odoo.delete(model, id)

    assert deleted == True
