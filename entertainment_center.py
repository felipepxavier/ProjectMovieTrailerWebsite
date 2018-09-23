# coding: utf-8

# importa o módulo "media", para criar as instancias.
import media

"""importa o módulo "fresh_tomatoes",
arquivo responsável por criar a página web."""
import fresh_tomatoes

"""criando uma instancia da classe Movie,
com seus devidos argumentos necessários."""
policial_em_apuros_2 = media.Movie(
    "Policial em Apuros 2", "Rookie"
    " Lawman Ben Barber deseja tornar-se um detetive, assim como"
    " James Payton, seu futuro cunhado. Relutantemente,"
    " James leva Ben para Miami em busca de pistas sobre "
    "um cartel de drogas. Durante a investigação, eles"
    " encontram evidências que implicam um respeitado"
    " empresário. Cabe a James e Ben provarem que o executivo"
    " carismático, Antonio Papa, é um violento senhor do crime"
    " que comanda o tráfico de drogas no Sul da Flórida.",
    "https://bit.ly/2liMyrS",
    "https://youtu.be/l9e96RAPMRM")

gente_grande = media.Movie(
    "Gente Grande", "A morte do treinador de basquete da infância"
    " de velhos amigos os reúne no mesmo lugar que celebraram um"
    " campeonato anos atrás. Os amigos, acompanhados de suas esposas"
    " e filhos, descobrem que idade não significa o mesmo que maturidade.",
    "https://bit.ly/2A6vVua",
    "https://youtu.be/HKVve_VSz58")

a_era_do_gelo = media.Movie(
    "A Era do Gelo", "Vinte mil anos atrás, num mundo coberto de gelo,"
    " o mamute Manfred e a preguiça Sid resgatam um bebê humano órfão."
    " Agora, os dois vão enfrentar muitas aventuras até devolver "
    "o filhote de gente à sua tribo, que migrou para um novo acampamento.",
    "https://bit.ly/2uTWoVU",
    "https://youtu.be/Zb3ZXTIgQCg")

deadpool = media.Movie(
    "Deadpool", "Wade Wilson é um ex-agente especial que passou a"
    " trabalhar como mercenário. Seu mundo é destruído quando um"
    " cientista maligno o tortura e o desfigura completamente."
    " O experimento brutal transforma Wade em Deadpool, que ganha"
    " poderes especiais de cura e uma força aprimorada. Com a ajuda"
    " de aliados poderosos e um senso de humor mais desbocado e cínico"
    " do que nunca, o irreverente anti-herói usa habilidades e métodos "
    "violentos para se vingar do homem que quase acabou com a sua vida.",
    "https://bit.ly/2mAE8gA",
    "https://youtu.be/Q9X-bAE8KTc")

harold = media.Movie(
    "Harold", "Aos 13 anos de idade, Harold está em um período de "
    "transformações, mas não contava com uma calvície prematura. "
    "Para piorar, ele ainda está se adaptando à nova escola e"
    " se transforma no alvo das piadas dos alunos.",
    "https://bit.ly/2Lz5xxz",
    "https://youtu.be/3OUytrApfFs")

madagascar = media.Movie(
    "Madagascar", "O leão Alex é o rei da selva urbana, a principal"
    " atração no zoológico de Nova York. Ele e seus melhores amigos"
    " - a zebra Marty, a girafa Melman e a hipopótamo fêmea Gloria"
    " - sempre viveram em cativeiro, felizes, com refeições regulares"
    " e um público para adorá-los. No entanto, Marty quer explorar"
    " o mundo e foge com a ajuda dos pinguins.",
    "https://bit.ly/2Ls5ByU",
    "https://youtu.be/ih7m3nO68_Y")

# criando uma lista e atribuindo todas as instancias da classe Movie.
movies = [policial_em_apuros_2, gente_grande,
          a_era_do_gelo, deadpool, harold, madagascar]

"""chamando a função "open_movies_page", localizada no módulo
"fresh_tomatoes", e dando de argumento a lista com todas as instancias"""
fresh_tomatoes.open_movies_page(movies)
