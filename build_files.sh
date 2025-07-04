# build_files.sh

#!/bin/bash

# Use the default Python and pip available in Vercel's build environment
pip install -r requirements.txt

# Run collectstatic to gather static files
python manage.py collectstatic --noinput
