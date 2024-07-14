"""
class Pessoa
    __init__
        nome str
        sobrenome str
        dados_obtidos bool

    API:
        obter_todos_os_dados -> method
            OK
            404    
"""
try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
            )
        )
    )
except:
    raise

import unittest
from unittest.mock import patch
from pessoa import Pessoa

class TestPessoa(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = Pessoa('Eduardo','Costa')
        self.p2 = Pessoa(data=True)
        self.p3 = Pessoa('Eduardo')
        return super().setUp()
    #tests
    def test_pessoa_correct_attr_nome(self):
        self.assertEqual(self.p1.nome,'Eduardo')    

    def test_pessoa_correct_attr_sobrenome(self):
        self.assertEqual(self.p1.sobrenome,'Costa')

    def test_pessoa_data_default_false(self):
        self.assertFalse(self.p1.data)        
        self.assertFalse(self.p3.data)

    def test_pessoa_data_true(self):
        self.assertTrue(self.p2.data)

    def test_pessoa_attr_str(self):
        self.assertIsInstance(self.p1.nome,str)
        self.assertIsInstance(self.p2.nome,str)
        self.assertIsInstance(self.p3.nome,str)

        self.assertIsInstance(self.p1.sobrenome,str)
        self.assertIsInstance(self.p2.sobrenome,str)
        self.assertIsInstance(self.p3.sobrenome,str)

    def test_pessoa_data_connection_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.getData(),'CONNECTED')
            self.assertTrue(self.p1.data)

    def test_pessoa_data_connection_fail(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.getData(),'ERROR 404')
            self.assertFalse(self.p1.data)

    def test_pessoa_data_connection_fail_and_success(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.getData(),'CONNECTED')
            self.assertTrue(self.p1.data)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.getData(),'ERROR 404')
            self.assertFalse(self.p1.data)
            



if __name__ == '__main__':
    unittest.main(verbosity=2)