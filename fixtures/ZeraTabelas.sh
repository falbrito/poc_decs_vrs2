
echo "Esse processo apagara todas as tabelas"
python ../manage.py flush


echo
echo "Cria superusuario"
python ../manage.py createsuperuser


echo
echo "Faz carregamento da tabela thesaurus"
python ../manage.py loaddata init_load/teste_thesaurus_migra.json
