#!/bin/bash

echo -e "\e[93mSetup stephlin/webvirtcloud image ...\e[0m"
docker build --tag stephlin/webvirtcloud .

echo -e "\e[93mSetup stephlin/webvirtcloud volumes ...\e[0m"
docker run --rm -itd --name webvirt-init stephlin/webvirtcloud
docker cp -a webvirt-init:/srv/webvirtcloud volume-webvirtcloud
docker cp -a webvirt-init:/var/www/.ssh volume-ssh
docker stop webvirt-init

docker-compose up -d
docker-compose exec webvirtcloud chown -R www-data /srv/webvirtcloud
docker-compose exec webvirtcloud chown -R www-data /var/www/.ssh
docker-compose down

echo -e "\e[93mFinished.\e[0m"
