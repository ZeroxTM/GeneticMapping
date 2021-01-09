"""
 @Time : 09/01/2021 16:10
 @Author : Alaa Grable
 """

import unittest


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


class TestSum(unittest.TestCase):

    # Test 1: Validate data filtering
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    def test_filtered_number(self):
        with open("C:\\Users\\alaat\\PycharmProjects\\GeneticMapping\\project_filter.txt", 'r') as file1:
            with open("C:\\Users\\alaat\\PycharmProjects\\GeneticMapping\\manual_filter.txt", 'r') as file2:
                same = set(file1).intersection(file2)
        self.assertEqual(len(same), 0, "Should be 0")

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    # Test 2: Validate sub-division
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    def test_subdivision(self):
        exists = 0
        marker = '"' + "NODE_6320_length_10694_cov_2.54404_B0_start3770,3911" + '"'
        with open("C:\\Users\\alaat\\PycharmProjects\\GeneticMapping\\linear_s.txt", 'r') as file:
            for line in file:
                if marker in line:
                    exists = 1
                    break
        self.assertEqual(exists, 0, "Should be 0")

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    # Test 3: Validate input file
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    def test_input_file(self):
        with open("C:\\Users\\alaat\\PycharmProjects\\GeneticMapping\\geneticMap.txt", 'r') as file:
            header = file.readline().split()
            result = header[0] == 'im' and header[1] == 'marker' and header[2] == 'bGood' and header[3] == 'iLG' \
                     and header[4] == 'chr' and header[5] == 'coorGenet' and header[6] == 'startCtgOnChr' \
                     and header[7] == 'indexOnPath'
            self.assertEqual(len(header), 8, "Should be 8")
            self.assertEqual(result, True, "Header should be different")
            for line in file:
                line = line.split()
                result = line[0].isdigit() and (True if line[2] in ["True", "False"] else False) and line[3].isdigit() and \
                         line[4].startswith("chr") and is_number(line[5]) and is_number(line[6]) and is_number(line[7])
                self.assertEqual(result, True, "Wrong data type")
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    # Test 4: Validate alleles file
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    def test_alleles_file(self):
        with open("C:\\Users\\alaat\\PycharmProjects\\GeneticMapping\\gPP.txt", 'r') as file:
            for line in file:
                line = line.split()
                self.assertEqual(len(line), 2, "Should be 2")
                matched_list = all([characters in ["0", "1", "-"] for characters in line[1]])
                self.assertEqual(matched_list, True, "Wrong data type")

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    # Test 5: Validate MST
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    def test_MST(self):
        pass
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


if __name__ == '__main__':
    unittest.main()
