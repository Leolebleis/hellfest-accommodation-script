from client import hellfest_client
from email_service import formatter
from filters import filter_accommodations


if __name__ == '__main__':
    filtered_accommodations = hellfest_client.accommodations_all()
    print(filter_accommodations(filtered_accommodations))
    formatter.render_accommodations()
