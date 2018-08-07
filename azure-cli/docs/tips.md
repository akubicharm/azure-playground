# VMの操作

## リソースグループ内のVMの起動と停止


### 起動
リソースグループを指定して一覧を取得し、 start の --ids オプションにしているする
```
az vm start --ids `az vm list -g openshift --query "[].id" -o tsv`
```


### 停止
リソースグループを指定して一覧を取得し、 deallocate の --ids オプションにしているする
```
az vm deallocate --ids `az vm list -g openshift --query "[].id" -o tsv`
```



### IP アドレスの取得
```
az vm list-ip-addresses -g yourResourceGroup -o table
```


## OpenShift関連

ARMのテンプレートでデプロイしたあとで、バージョンを変えたり色々やりたい場合には、bastionノードから、サーバーの管理をansibleのワンライナーでやるとちょっと便利。

```
ansible --list-hosts nodes
```


subscriptionの確認
```
ansible nodes -b -a 'subscription-manager status'
```

```
ansible nodes -b -a 'subscription-manager repos --disable="rhel-7-server-ose-3.9-rpms"'
ansible nodes -b -a 'subscription-manager repos --enable="rhel-7-server-ose-3.10-rpms"'
```
