# coding: utf-8

# módulo responsável por abrir a página web.
import webbrowser


class Movie():
    """ Esta classe fornece uma maneira de
    armazenar informações relacionadas a filmes """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """ Método construtor, responsável por definir
        qual assinatura a classe deve conter ao ser instanciada."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        # função responsável por abrir o trailer dos filmes
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)