class API_Constants:

    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def create_booking_url():
        return "https://restful-booker.herokuapp.com/booking"

    def create_token(self):
        return "https://restful-booker.herokuapp.com/auth"


    def put_patch_delete_get(booking_id):
        return "https://restful-booker.herokuapp.com/booking/"+ str(booking_id)

