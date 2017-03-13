# SMTP to API

An adaptor for legacy applications to work with email API vendors.
Particularly useful in cases when SMTP ports are blocked on the server or network.

At the moment in works  with Mailgun API and with limited features.

## Getting Started

1. Clone this repository to a location where you want to install the application
2. Follow commands in `Makefile` or just run `make install` to create a virtual environment and install dependencies
3. Copy `smtp2api.example` to `/etc/init.d/smtp2api` with this command: `sudo cp smtp2api.example /etc/init.d/smtp2api`
4. Update `/etc/init.d/smtp2api` with your desirable configuration
5. Copy `config.ini.example` to `config.ini`
6. Update `config.ini` with your vendor, domain/login and api key
7. Run service with `sudo service smtp2api start` or run it from the directory with `make run` for debugging purpose

This project is in WIP status. Pull requests are welcome.