from xmlrpc import client
from typing import List, Dict


class OdooAPI:

    def __init__(self, server, database_name, username, access_token, node='object'):
        self.server = server
        self.db = database_name
        self.access_token = access_token
        self.uid = self.get_user_id(username)
        self.client = self._get_client(node)

    def get_user_id(self, username):
        common = self._get_client('common')
        return common.authenticate(self.db, username, self.access_token, {})

    def _get_client(self, node):
        return client.ServerProxy(f'{self.server}/xmlrpc/2/{node}')

    def execute(self, model, method, *args):
        return self.client.execute_kw(self.db, self.uid, self.access_token, model, method, *args)

    def read(self, model: str, record_ids: list, fields: list, *args):
        """
        This object read model data using record id

        Parameters
        ~~~~~~~~~~
        model: str
            Odoo object model. For example, sale.order

        record_list: list
            A list of ids of model entry

        fields: list
            A list of model fields

        Returns
        ~~~~~~~
        List of records
        A list of dictionary for the relevant model

        """

        return self.execute(model, 'read', [record_ids], dict(fields=fields), *args)

    def search(self, model: str, logic: list, *args):
        """
        This object search model data using the logic provided 

        Parameters
        ~~~~~~~~~~
        model: str
            Odoo object model. For example, sale.order

        logic: list
            A mandatory domain filter to grab a single record or list of records. 
                For example, ['name', '=', 'Democustomer'] or ['id', '>', '1']

        *args: dict // optional
            By default, search returns all the records matching the condition. This parameter is 
            used to only retrieve a subset of all matched records. {'limit':5}

        Returns
        ~~~~~~~
        List of ids 
            The database identifiers of all records matching the filter.

        """
        return self.execute(model, 'search', [[logic]], *args)

    def search_read(self, model, logic: list, fields: list, **extra):
        """
        Searches for the model data using domain filter and returns the data of all records 
        matching the filter.

        Parameters
        ~~~~~~~~~~
         model: str
            Odoo object model. For example, sale.order

        logic: list
            A mandatory domain filter to grab a single record or list of records. 
                For example, ['name', '=', 'Democustomer'] or ['id', '>', '1']

        fields: list
            A list of model fields

        **extra: 
            key to retrieve a subset of data. Ex - limit = 5 
        
        
        Returns
        ~~~~~~~
        List of records
            A list of dictionary for the relevant model
        
        """
        return self.execute(model, 'search_read', [[logic]], {'fields': fields, **extra})

    def get_fields(self, model, fields=None, attributes=None):
        """This object can be used to inspect a model's fields and 
        check which ones seem to be of interest.
        
        Parameters
        ~~~~~~~~~~
        model: str
            Odoo object model. For example, sale.order
            
        fields: list
            A list of model fields
        
        attributes: list
            A list of model fields

        Returns
        ~~~~~~~
        A dictionary, where all the metainformation about the fields are retrieved.
                
        """
        args = [model, 'fields_get']
        fields = fields if fields else []
        args.append(fields)

        if attributes:
            args.append(dict(attributes=attributes))

        return self.execute(*args)

    def create(self, model, records: List[Dict]):
        """
        The method creates a single record and returns its database identifier.

        Parameters
        ~~~~~~~~~~~
        model: str
            Odoo object model. For example, sale.order

        records: List[Dict]
            List of dictionary containing all the attribute
        
        Returns
        ~~~~~~~~~~~
        List of ids of records created

        """
        return self.execute(model, 'create', records)

    def update(self, model, record_ids: list, **kwargs):
        """
        This object is used to update a list of records

        Parameters
        ~~~~~~~~~~
        model: str
            Odoo object model. For example, sale.order
        
        record_list: list
            A list of ids of model entry
        
        kwargs: dict
            Dictionary fields to update
        
        Returns
        ~~~~~~~
        Boolean : True or False
        """
        return self.execute(model, 'write', [record_ids, kwargs])

    def delete(self, model, record_ids: list):
        """
        This object can delete bulk of records with their ids.

        Parameters
        ~~~~~~~~~~
        model: str
            Odoo object model. For example, sale.order
        
        record_list: list
            A list of ids of model entry
        
        Returns
        ~~~~~~~
        Boolean : True or False
        
        """

        return self.execute(model, 'unlink', [record_ids])
