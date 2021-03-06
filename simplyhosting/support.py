from .request import Request


class Support(object):
    def __init__(self, apiClient):
        self.apiClient = apiClient

    def get_active_tickets(self, optional_data={}):
        request = Request('post', '/support/getActiveTickets')
        request.data = optional_data
        self.apiClient.request = request
        return self.apiClient

    def get_tickets(self, limit, optional_data={}):
        request = Request('post', '/support/getTickets')
        request.data = {'limit': limit}
        request.data.update(optional_data)
        self.apiClient.request = request
        return self.apiClient

    def search(self, data={}):
        request = Request('post', '/support/search')
        request.data = data
        self.apiClient.request = request
        return self.apiClient

    def get_ticket(self, ticket_id):
        request = Request('post', '/support/getTicket')
        request.data = {'ticketId': ticket_id}
        self.apiClient.request = request
        return self.apiClient

    def reply_ticket(self, ticket_id, text):
        request = Request('post', '/support/replyTicket')
        request.data = {'ticketId': ticket_id, 'text': text}
        self.apiClient.request = request
        return self.apiClient

    def update_ticket_priority(self, ticket_id, priority):
        request = Request('post', '/support/updateTicketPriority')
        request.data = {'ticketId': ticket_id, 'priority': priority}
        self.apiClient.request = request
        return self.apiClient

    def close_ticket(self, ticket_id):
        request = Request('post', '/support/closeTicket')
        request.data = {'ticketId': ticket_id}
        self.apiClient.request = request
        return self.apiClient

    def create_ticket(self, subject, text, optional_data={}):
        request = Request('post', '/support/createTicket')
        request.data = {'subject': subject, 'text': text}
        request.data.update(optional_data)

        self.apiClient.request = request
        return self.apiClient

    def update_ticket(self, ticket_id, optional_data={}):
        request = Request('post', '/support/updateTicket')
        request.data = {'ticketId': ticket_id}
        request.data.update(optional_data)

        self.apiClient.request = request
        return self.apiClient

    def forward_to_ph(self, ticket_id):
        request = Request('post', '/support/forwardToPH')
        request.data = {'ticketId': ticket_id}

        self.apiClient.request = request
        return self.apiClient

    def forward_to_ph_remove(self, ticket_id):
        request = Request('post', '/support/forwardToPHRemove')
        request.data = {'ticketId': ticket_id}

        self.apiClient.request = request
        return self.apiClient
