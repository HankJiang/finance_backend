常见问题
-

#### 相关依赖

 - `pipreqs` 检查项目依赖，生成requirements.txt 

#### 本地启动

 - 方式1
 
    ```bash
     > export FLASK_ENV=development
     > flask run
    ```
 
 - 方式2：使用gunicorn
 
    - -c CONFIG, --config=CONFIG # 设定配置文件。
    - -b BIND, --bind=BIND # 设定服务需要绑定的端口。建议使用HOST:PORT。
    - -w WORKERS, --workers=WORKERS  # 设置工作进程数。建议服务器每一个核心可以设置2-4个。
    
    ```bash
     > gunicorn -w 2 -b 127.0.0.1:8080 app:app
    ```
   
 #### 使用Docker
 
 - 镜像构建
 
     - `> docker build -t local-image:tagname .` 基于当前目录dockerfile
     - `> docker tag local-image:tagname remote-repo:tagname`
     - `> docker push remote-repo:tagname`
 
 - 使用镜像
    - `> docker pull remote-image:tagname`
    - `> docker login -u username -p password` 私有仓库先登录
    - `> docker run -p local-port:contaner-port -d image-id`
    
 - 使用 volume 
    
    
 #### 使用K8S
 
 ##### kubeadm
 
  - 初始化
    
    ```bash
        kubeadm init --config kubeadm.yaml
    ```
 
 
 
 
 
 
 
 
 
 