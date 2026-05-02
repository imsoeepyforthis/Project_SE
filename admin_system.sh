#!/bin/bash

# admin_system.sh

# creation le account
create_user() {
echo "Entrez le nom de username:"
read username
sudo useradd -m $username
sudo passwd $username
echo "utilisateur $username créé avec succés!"
}

# le dossier
create_dossier() {
echo "Entrez le nom du dossier:"
read nom_dossier
sudo mkdir /home/$username/$nom_dossier
echo "Dossier créé dans /home/$username/$nom_dossier"
}

# code le permissions
set_permission() {
echo "Entrez le chemin du dossier:"
read chemin_dossier
sudo chmod 755 $chemin_dossier
sudo chown $username:$username $nom_dossier
echo "permissions définies avec succés!"
}

# quota (ha4e le 7ajem kemeye men memoire r eli lhi t36i le user)
set_quota() {
echo "Entrez le quota disque en MB pour $username:"
read taille_quota
sudo setquota -u $username 0  ${taille_quota}M ${taille_quota}M 00 -a
}

# menu
echo "Menu d'Adminstration"
echo "1. créer un nouvel username"
echo "2. créér un dossier"
echo "3. définir les permissions"
echo "4. définir le taille de quota"
echo "5. quitter"
echo "Choississez une option (1-5):"
read choix

case $choix in 
1) create_user ;;
2) create_dossier ;;
3) set_permission ;;
4) set_quota ;;
5) echo "Au revoir" exit ;;
*) echo ">:(" ;;
esac

