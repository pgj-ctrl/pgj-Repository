[
    {
        'name': 'configure webservers',
        'hosts': 'webservers',
        'tasks': [
            {
                'name': 'install httpd',
                'yum': {
                    'name': 'httpd',
                    'state': 'present'
                }
            },
            {
                'name': 'enable httpd service',
                'service': {
                    'name': 'httpd',
                    'state': 'started',
                    'enabled': 'yes'
                }
            }
        ]
    },
    {
        'name': 'configure dbservers',
        'hosts': 'dbservers',
        'tasks': [
            {
                'name': 'install mariadb-server',
                'yum': {
                    'name': 'mariadb-server',
                    'state': 'present'
                }
            },
            {
                'name': 'enable mariadb service',
                'service': {
                    'name': 'mariadb',
                    'state': 'started',
                    'enabled': 'yes'
                }
            }
        ]
    }
]