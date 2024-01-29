#!/usr/bin/env sh

doctl auth init -t "${DO_KUBERNETES_TOKEN}"
doctl kubernetes cluster kubeconfig save \
      "${DO_KUBERNETES_CLUSTER_ID}" \
      --expiry-seconds "${DO_KUBERNETES_CLUSTER_CREDENTIALS_EXPIRY}"

for p in $(kubectl get pods -n kube-system -o name | grep doks)
do
    kubectl -n kube-system exec -t  "${p}" -- bash -c "chroot /host sh -c 'apt-get install -y nfs-kernel-server'"
done

check_floating_ip_is_assigned.py
