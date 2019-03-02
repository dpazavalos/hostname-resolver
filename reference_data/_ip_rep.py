from typing import List, Tuple, NamedTuple
from collections import namedtuple


class IpReport:

    not_found = 'N / A'
    """Default value if unable to resolve a hostname"""
    # Pseudo constant. Used by SocketAnswer

    def __init__(self):

        self.valids: List[str] = []
        """IPs of valid Hostnames"""

        self.invalids: List[str] = []
        """Hostnames with no IP found"""

        self.hostnames_in: List[str] = []
        """List of given hostnames to resolve"""

        self.socket_answers: List[_SocketAnswer] = []
        """Answers to extended socket calls. Used for persistence against cumulative runs\n
        Ultimately, a list of socket_answers"""

        self.sock_ans = _SocketAnswer

    def reset(self):
        """Resets non persistent storage arrays"""
        self.valids.clear()
        self.invalids.clear()
        self.hostnames_in.clear()

    def reset_all(self):
        """Resets ALL storage arrays. Clean slate"""
        self.reset()
        self.socket_answers.clear()


class _SocketAnswer(NamedTuple):
    """
    Schematic for socket_answer named tuples. Build this and add to socket_answers
    Needs only given to build. FQDN and IP default to IpReport._not_found, must be overwritten

    Values:
        given: Given hostname used to get socket answer

        fqdn: given hostname and tld used successfully\

        ip: Found IP from fqdn
    """

    given: str
    fqdn: str = IpReport.not_found
    ip: str = IpReport.not_found

    def values(self):
        """Returns tuple of given, fqdn, ip"""  # Poor scaling, but of little concern here
        return self.given, self.fqdn, self.ip


class _IpReportFactory:
    """Factory method to create new IpReport object"""

    @staticmethod
    def _return_ip_report_obj():
        new_obj = IpReport()
        return new_obj

    def new_ip_report_obj(self, ):
        return self._return_ip_report_obj()

