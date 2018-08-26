import unittest.mock as mock
import mycity.test.test_constants as test_constants
import mycity.test.unit_tests.base as base
import mycity.utilities.gis_utils as gis_utils
import mycity.utilities.google_maps_utils as g_maps_utils


class GISUtilitiesTestCase(base.BaseTestCase):

    @mock.patch(
        'mycity.utilities.google_maps_utils.get_driving_info',
        return_value=test_constants.GOOGLE_MAPS_JSON
    )
    def test_get_closest_feature(self, mock_get_driving_info):
        test_origin = "46 Everdean St Boston, MA"
        test_features = [
            ['close', '94 Sawyer Ave Boston, MA'],
            ['far', '4 Olivewood Ct Greenbelt, MD']
        ]
        feature_address_index = 1
        feature_type = "test"
        error_message = "Test error message"
        result = gis_utils.get_closest_feature(
            test_origin,
            feature_address_index,
            feature_type,
            error_message,
            test_features
        )
        self.assertEqual(
            "94 Sawyer Ave Boston, MA",
            result[feature_type]
        )
        self.assertEqual(
            '7 mins',
            result[g_maps_utils.DRIVING_TIME_TEXT_KEY]
        )
        self.assertEqual(
            '1.5 mi',
            result[g_maps_utils.DRIVING_DISTANCE_TEXT_KEY]
        )

    def test_get_dest_addresses_from_features(self):
        to_test = \
            gis_utils._get_dest_addresses_from_features(
                test_constants.PARKING_LOTS_ADDR_INDEX,
                test_constants.PARKING_LOT_FEATURES
            )
        for address in to_test:
            self.assertTrue(address.find("Boston, MA"))

    ####################################################################
    # Tests that should only be run if we're connected to the Internet #
    ####################################################################

#     def test_get_features_from_feature_server(self):
#         url = ('https://services.arcgis.com/sFnw0xNflSi8J0uh/'
#                'ArcGIS/rest/services/SnowParking/FeatureServer/0')
#         query = '1=1'
#         test_set = location_utils.get_features_from_feature_server(url, query)
#         self.assertIsInstance(test_set[0], list)


#     def test_get_closest_feature(self):
#         origin = "46 Everdean St"
#         features = [ ["far", "19 Ashford St"],
#                   ["close", "94 Sawyer Ave"],
#                   ["closest", "50 Everdean St"] ]
#         address_index = 1
#         feature_type = "test_feature"
#         closest = location_utils.get_closest_feature(origin, address_index, 
#                                                      feature_type,
#                                                      "A fake error message",
#                                                      features)
#         self.assertEqual("50 Everdean St Boston, MA", closest[feature_type])
#         self.assertIsInstance(closest[location_utils.DRIVING_DISTANCE_TEXT_KEY],
#                               str)
#         self.assertIsInstance(closest[location_utils.DRIVING_TIME_TEXT_KEY],
#                               str)
#         # check to make sure DRIVING_DISTANCE and DRIVING_TIME are not 
#         # empty strings
#         self.assertNotEqual("", closest[location_utils.DRIVING_DISTANCE_TEXT_KEY])
#         self.assertNotEqual("", closest[location_utils.DRIVING_TIME_TEXT_KEY])

#     def test_get_closest_feature_with_error(self):
#         """
#         A call to get_closest_feature that fails should return a dict
#         with these key:value pairs
#             { feature_type: False,
#               DRIVING_DISTANCE_TEXT_KEY: False,
#               DRIVING_TIME_TEXT_KEY: False 
#             }
#         """
#         origin = "46 Everdean St"
#         features = [ ]
#         address_index = 1
#         feature_type = "test_feature"
#         closest = location_utils.get_closest_feature(origin, address_index,
#                                                      feature_type,
#                                                      "A fake error message",
#                                                      features)
#         self.assertFalse(closest[feature_type])
#         self.assertFalse(closest[location_utils.DRIVING_DISTANCE_TEXT_KEY])
#         self.assertFalse(closest[location_utils.DRIVING_TIME_TEXT_KEY])

