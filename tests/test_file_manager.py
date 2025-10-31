import unittest
import os
from src.file_manager import adicionar_documento, renomear_documento, remover_documento

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.diretorio = 'data'
        self.arquivo_teste = 'teste_unidade.txt'
    
    def test_adicionar(self):
        sucesso, msg = adicionar_documento(self.arquivo_teste, self.diretorio)
        self.assertTrue(sucesso)
        self.assertTrue(os.path.exists(os.path.join(self.diretorio, self.arquivo_teste)))
        os.remove(os.path.join(self.diretorio, self.arquivo_teste))  # Limpa
    
    def test_renomear(self):
        # Adiciona primeiro
        adicionar_documento(self.arquivo_teste, self.diretorio)
        sucesso, msg = renomear_documento(self.arquivo_teste, 'renomeado.txt', self.diretorio)
        self.assertTrue(sucesso)
        self.assertFalse(os.path.exists(os.path.join(self.diretorio, self.arquivo_teste)))
        os.remove(os.path.join(self.diretorio, 'renomeado.txt'))  # Limpa

if __name__ == '__main__':
    unittest.main()