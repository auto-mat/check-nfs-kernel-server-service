# K8 check-nfs-kernel-server-service Docker image

### Usage
K8 Cron job to check if the Kube POD system has the nfs-kernel-server
package installed (if it is not installed, it will install it) which
provide a kernel module for the correct operation of the NFS server.
With additional Digital Ocean floating IP address checking (if it is
not assigned, it will assign it).

### Build Docker check-nfs-kernel-server-service image and run container

```bash
# Build Docker image
docker buildx build -t auto0mat/check-nfs-kernel-server-service:<ACTUAL_YEAR>.<SERIAL_NUMBER> .

# Run Docker container
docker run -d --rm \
--env="DO_KUBERNETES_TOKEN=<CHANGE_IT>" \
--env="DO_KUBERNETES_CLUSTER_ID=<CHANGE_IT>" \
--env="DO_KUBERNETES_CLUSTER_CREDENTIALS_EXPIRY=<CHANGE_IT>" \
--env="DO_FLOATING_IP_ADDRESS=<CHANGE_IT>" \
--name=check-nfs-kernel-server-service \
auto0mat/check-nfs-kernel-server-service:latest
```

### Licence

[GNU AGPLv3](https://www.gnu.org/licenses/agpl-3.0.en.html) or later.
