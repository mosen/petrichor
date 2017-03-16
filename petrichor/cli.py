import os
import argparse

def main():
    parser = argparse.ArgumentParser(
        description='Petrichor - CDP Sync Tool',
    )
    parser.add_argument('--url', dest='url', help='URL to your JSS (env JSS_URL)',
                        default=os.environ.get('JSS_URL', None))
    parser.add_argument('--username', dest='username', help='JSS Username (env JSS_USERNAME)',
                        default=os.environ.get('JSS_USERNAME', None))
    parser.add_argument('--password', dest='password', help='JSS Password (env JSS_PASSWORD)',
                        default=os.environ.get('JSS_PASSWORD', None))

    