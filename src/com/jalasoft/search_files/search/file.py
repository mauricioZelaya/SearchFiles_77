"""

"""

from src.com.jalasoft.search_files.search.asset import Asset


class File(Asset):
    """

    """
    def set_file_name(self, file_name):
        """

        :param file_name:
        :return:
        """
        self._file_name = file_name

    def set_file_size(self, file_size):
        """

        :param file_size:
        :return:
        """
        self._file_size = file_size

    def set_is_directory(self, is_directory):
        """

        :param is_directory:
        :return:
        """
        self.is_directory = is_directory