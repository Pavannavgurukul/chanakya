ENV="development"
USER=itsdubu
FLASK_MODULE='chanakya.src'

export FLASK_ENV=$ENV
export CHANAKYA_ENVIRONMENT=$ENV

APP_PATH=/home/$USER/chanakya

cd /home/$USER/
source $APP_PATH/venv/bin/activate
$APP_PATH/venv/bin/gunicorn ${FLASK_MODULE}:app --bind=0.0.0.0:5000
