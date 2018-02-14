"""

"""

from src.com.jalasoft.search_files.search.asset import Asset


class Folder(Asset):
    """

    """

    def set_file_name(self, file_name):
        """

        :param file_name:
        :return:
        """
        self._file_name = file_name

    def set_is_directory(self, is_directory):
        """

        :param is_directory:
        :return:
        """
        self.is_directory = is_directory
