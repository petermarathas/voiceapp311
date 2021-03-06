"""
Uses ArcGIS to find location based information about Boston city services
"""

from mycity.utilities.finder.Finder import Finder 


class FinderGIS(Finder):
    
    """
    Finder subclass to find Feature locations from ArcGIS Feature Server
    
    @property: query ::= parameter for call to ArcGIS server

    """

    default_query = "1=1"               # default query returns all records


    def __init__(self, req, resource_url, address_key, output_speech,
                 output_speech_prep_func, query = FinderGIS.default_query):
        """
        Call super constructor and save query

        :param req: MyCityRequestDataModel
        :param resource_url: String that Finder classes will 
            use to GET or query from
        :param address_key: string that names the type of 
            location we are finding
        :param output_speech: String that will be formatted later
            with closest location to origin address. NOTE: this should
            be formatted using keywords as they are expected to appear
            as field in the CSV file or Feature fetched from ArcGIS
            FeatureServer
        :param output_speech_prep_func: function that will access
            and modify fields in the returned record for output_speech
            formatted string
        :param query: parameter for call to ArcGIS server 
        """
        super().__init__(req, resource_url, address_key, output_speech,
                         output_speech_prep_func)
        self.query = query


    def get_records(self):
        """
        Query City of Boston Feature Server, and return a list of features
        
        :return: list of features corresponding to query
        """
        print("[method: FinderGIS.get_features_from_feature_server]")
        return gis_utils.get_features_from_feature_server(self.resource_url,
                                                          self.query)
