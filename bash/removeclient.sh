function revokeClient() {
    if [[ $# -eq 0 ]]; then
        echo "Please provide a user argument."
        exit 1
    fi

    USERNAME="$1"

    NUMBEROFCLIENTS=$(tail -n +2 /etc/openvpn/easy-rsa/pki/index.txt | grep -c "^V")
    if [[ $NUMBEROFCLIENTS == '0' ]]; then
        echo ""
        echo "You have no existing clients!"
        exit 1
    fi

    CLIENTNUMBER=$(tail -n +2 /etc/openvpn/easy-rsa/pki/index.txt | grep -n "^V" | grep "$USERNAME" | cut -d ':' -f 1)
    if [[ -z $CLIENTNUMBER ]]; then
        echo ""
        echo "Client $USERNAME not found!"
        exit 1
    fi

    echo ""
    echo "Revoking certificate for client $USERNAME"
    CLIENT=$(tail -n +2 /etc/openvpn/easy-rsa/pki/index.txt | grep "^V" | cut -d '=' -f 2 | sed -n "$CLIENTNUMBER"p)
    cd /etc/openvpn/easy-rsa/ || return
    ./easyrsa --batch revoke "$CLIENT"
    EASYRSA_CRL_DAYS=3650 ./easyrsa gen-crl
    rm -f /etc/openvpn/crl.pem
    cp /etc/openvpn/easy-rsa/pki/crl.pem /etc/openvpn/crl.pem
    chmod 644 /etc/openvpn/crl.pem
    find /home/ -maxdepth 2 -name "$CLIENT.ovpn" -delete
    rm -f "/root/$CLIENT.ovpn"
    sed -i "/^$CLIENT,.*/d" /etc/openvpn/ipp.txt
    cp /etc/openvpn/easy-rsa/pki/index.txt{,.bk}

    echo ""
    echo "Certificate for client $CLIENT revoked."
}

revokeClient "$1"
