from django.urls import reverse


class TestViews:

	url = reverse("list_s3_documents:index")

	def test_index(self, client):
		response = client.get(self.url)
		print(response.content)
