#!/bin/bash
# -------------------------------------------------------------------------- #
# gera_fixture_biblioref_ALL.sh - Realiza conversao de registro ISIS para JSON
# -------------------------------------------------------------------------- #
#    Corrente : serverofi5:/bases/fiadmin/migration/lilacs
#     Chamada : gera_fixture_biblioref_ALL.sh <arquivo iso> <[sas|mnt]>
#     Exemplo : ./gera_fixture_biblioref_ALL.sh LILACS_SAMPLE.iso sas
#
# -------------------------------------------------------------------------- #
#  Centro Latino-Americano e do Caribe de Informação em Ciências da Saúde
#     é um centro especialidado da Organização Pan-Americana da Saúde,
#           escritório regional da Organização Mundial da Saúde
#                      BIREME / OPS / OMS (P)2016
# -------------------------------------------------------------------------- #

# Historico
# versao data, Responsavel
#       - Descricao
cat > /dev/null <<HISTORICO
vrs:  1.00 20160811, Ana Katia Camilo - Fabio Luis de Brito
        - Edicao original
HISTORICO

# -------------------------------------------------------------------------- #

INSUMO="arquivos_json_qualificadores"


echo
echo "ATENCAO! Esse processo fara a inclusao de conteudo no FI-Admin"
echo "Esta lendo o insumo de fixtures/$INSUMO/slice*.json"
echo
echo "Se houver duvida digite CTRL+c, ou Enter para continuar."
read #pausa até que o ENTER seja pressionado

# read -p "Este procedimento irá IMPORTAR os dados. Confirma (S/N)? " -n 1 -r


# -------------------------------------------------------------------------- #

# Anota hora de inicio de processamento
export HORA_INICIO=`date '+ %s'`
export HI="`date '+%Y.%m.%d %H:%M:%S'`"

echo "[TIME-STAMP] `date '+%Y.%m.%d %H:%M:%S'` [:INI:] Processa ${0} ${1} ${3} ${4} ${5}"
echo ""
# ------------------------------------------------------------------------- #




export PYTHONWARNINGS="ignore::DeprecationWarning"
# source /home/apps/bvsalud-org/fi-admin-curso/env/bin/activate

# Acessando diretorio dos arquivos json
cd $INSUMO

# criando lista de arquivos
ls slice*json > lista.lst
numero_arquivos=`cat lista.lst | wc -l`

# voltando diretorio de execucao
cd -

contador=1
for arq in $(cat $INSUMO/lista.lst)
do

  echo "Importando: $arq ( $contador de $numero_arquivos )"

  python ../manage.py loaddata $INSUMO/$arq
  if [ "$?" -ne 0 ]
  then
    echo "Houve erro na importacao! - ver arquivo: $arq"
    mv $INSUMO/$arq $INSUMO/fix_$arq
  fi

  contador=`expr $contador + 1`

done

# verificando se existem arquivos com erro
echo
echo "Analisando arquivos que nao foram importados no FI-Admin ..."
# Verifica se existe o arquivo
if [ $(ls $INSUMO/fix_* 2> /dev/null | wc -l) -eq 0 ]
then
  echo " Importacao OK!!!"
else
  ls $INSUMO/fix_*

  total_fix=`grep decs_code $INSUMO/fix_* | awk -F":" '{ print $3 }' | sed 's/\"//g' | sed 's/\,//g' | sed 's/ //g' | wc -l`

  echo "Total de fix´s"
  echo "$total_fix"

fi

echo
echo "Total de id´s"
grep decs_code $INSUMO/slice*.json | awk -F":" '{ print $3 }' | sed 's/\"//g' | sed 's/\,//g' | sed 's/ //g' | wc -l


HORA_FIM=`date '+ %s'`
DURACAO=`expr ${HORA_FIM} - ${HORA_INICIO}`
HORAS=`expr ${DURACAO} / 60 / 60`
MINUTOS=`expr ${DURACAO} / 60 % 60`
SEGUNDOS=`expr ${DURACAO} % 60`

echo
echo "DURACAO DE PROCESSAMENTO"
echo "-------------------------------------------------------------------------"
echo " - Inicio:  ${HI}"
echo " - Termino: `date '+%Y.%m.%d %H:%M:%S'`"
echo
echo " Tempo de execucao: ${DURACAO} [s]"
echo " Ou ${HORAS}h ${MINUTOS}m ${SEGUNDOS}s"
echo

# ------------------------------------------------------------------------- #
echo "[TIME-STAMP] `date '+%Y.%m.%d %H:%M:%S'` [:FIM:] Processa  ${0} ${1} ${3} ${4} ${5}"
# ------------------------------------------------------------------------- #
echo
echo




exit

# Fabio
python manage.py loaddata arquivos_json/*.json

