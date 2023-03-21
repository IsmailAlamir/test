echo " BUILD START"
puthon3.9 -m pip install -r requirements.txt
puthon3.9 manage.py collectstatic --noinput --clear
echo " BUILD END"
