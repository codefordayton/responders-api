import logging

from django.contrib.gis.geos import GEOSGeometry
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from user_data.models import ExtendedUserData
from geocode.models import ZipGeocode

logger = logging.getLogger(__name__)


class MessageUsers(APIView):
    """
    Handle message distribution for emergency alerts

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    #authentication_classes = (authentication.TokenAuthentication,)
    #permission_classes = (permissions.IsAdminUser,)

    def get(self, request, zip, radius, format=None):
        """Return a list of all users that would be messaged for a zip / radius

        :param request:
        :param zip:
        :param radius:
        :param format:
        :return:
        """

        extended_users = self._get_users(zip, radius)

        users = []
        for user in extended_users:
            user_info = {}
            user_info['name'] = user.user.first_name + ' ' + user.user.last_name
            user_info['zip'] = user.zip_code
            user_info['location'] = user.location.wkt
            users.append(user_info)

        return Response(users)

    def post(self, request, zip, radius, format=None):
        """Send a message to all users that would be messaged for a zip / radius

        :param request:
        :param zip:
        :param radius:
        :param format:
        :return:
        """

        message = request.data['message']
        print request.data

        extended_users = self._get_users(zip, radius)

        logger.debug('received a message of %s' % message)

        for user in extended_users:
            logger.debug('attempting to send message')
            user.send_message_to(message)

        return Response(status.HTTP_202_ACCEPTED)

    @staticmethod
    def _get_users(zip, radius):
        """Identify users for a zip radius

        :param zip:
        :param radius:
        :return:
        """
        radius = float(radius)
        logger.debug('finding users within %s miles of zip code %s' % (radius, zip))

        zipcode = ZipGeocode.objects.get(pk=zip)
        geom = GEOSGeometry('POINT(%s %s)' % (zipcode.longitude, zipcode.latitude))
        buffered_geom = geom.buffer(radius)

        extended_users = ExtendedUserData.objects.filter(location__intersects=buffered_geom)

        return extended_users


class MessageUsersJson(APIView):
    """
    Handle message distribution for emergency alerts

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    #authentication_classes = (authentication.TokenAuthentication,)
    #permission_classes = (permissions.IsAdminUser,)


    def get(self, request, format=None):
        """Return a list of all users that would be messaged for a zip / radius

        :param request:
        :param format:
        :return:
        """

        #logger.debug('finding users within %s miles of zip code %s' % (radius, zip))

        #usernames = [user.username for user in User.objects.all()]
        #return Response(usernames)