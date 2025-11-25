import unittest
import werkzeug

from app import app
from flask_jwt_extended import decode_token

# Patch temporário para compatibilidade com Flask + Werkzeug
if not hasattr(werkzeug, "__version__"):
    werkzeug.__version__ = "mock-version"


class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cria o client uma vez só para todos os testes
        cls.app = app
        cls.client = app.test_client()

    def test_home_status_e_mensagem(self):
        """Verifica status 200 e mensagem correta na rota /"""
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

        data = resp.get_json()
        self.assertIn("message", data)
        self.assertEqual(data["message"], "API is running")

    def test_items_retorna_lista_de_tres_itens(self):
        """Garante que /items retorna uma lista com 3 itens específicos"""
        resp = self.client.get("/items")
        self.assertEqual(resp.status_code, 200)

        data = resp.get_json()
        self.assertIn("items", data)
        self.assertIsInstance(data["items"], list)
        self.assertEqual(len(data["items"]), 3)
        self.assertListEqual(data["items"], ["item1", "item2", "item3"])

    def test_login_retorna_jwt_valido(self):
        """
        Verifica se /login retorna um token JWT não vazio
        e se o token decodificado tem a identidade esperada.
        """
        resp = self.client.post("/login")
        self.assertEqual(resp.status_code, 200)

        body = resp.get_json()
        self.assertIn("access_token", body)

        token = body["access_token"]
        self.assertIsInstance(token, str)
        self.assertGreater(len(token), 0)

        # decodifica o token dentro do contexto da app
        with self.app.app_context():
            decoded = decode_token(token)
            # 'sub' é o subject (identity) padrão do flask_jwt_extended
            self.assertEqual(decoded["sub"], "user")

    def test_protected_sem_token_retorna_401(self):
        """Garante que /protected sem token retorna 401 (não autorizado)."""
        resp = self.client.get("/protected")
        self.assertEqual(resp.status_code, 401)

    def test_protected_com_token_valido(self):
        """
        Faz login, pega o token e acessa /protected com Authorization: Bearer <token>.
        Deve retornar 200 e a mensagem esperada.
        """
        login_resp = self.client.post("/login")
        token = login_resp.get_json()["access_token"]

        headers = {"Authorization": f"Bearer {token}"}
        resp = self.client.get("/protected", headers=headers)

        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn("message", data)
        self.assertEqual(data["message"], "Protected route")

    def test_rota_inexistente_retorna_404(self):
        """Chama uma rota que não existe e verifica se retorna 404."""
        resp = self.client.get("/rota_que_nao_existe")
        self.assertEqual(resp.status_code, 404)


if __name__ == "__main__":
    unittest.main()
