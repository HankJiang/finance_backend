常见问题
-

#### 相关依赖

 - `pipreqs` 检查项目依赖，生成requirements.txt

<br>


#### 使用Celery
    

<br>

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
  
 <br>
 
 #### 使用docker 
 
 ##### 通过镜像仓库
 - 镜像构建
 
     - `> docker build -t local-image:tagname .` 基于当前目录dockerfile
     - `> docker tag local-image:tagname remote-repo:tagname`
     - `> docker push remote-repo:tagname`
 
 - 使用镜像
    - `> docker pull remote-image:tagname`
    - `> docker login -u username -p password` 私有仓库先登录
    - `> docker run -p local-port:contaner-port -d image-id`
    
##### （线上环境）通过webhook拉取项目到本地构建
 
 
 <br>
 
 #### 使用docker-compose
 
  - volume:
 
   -  可以让容器之间或者容器和宿主机之间共享数据
   -  通过`docker volume create volume_name`创建命名卷，
      这种方式会自动在宿主机docker目录下创建数据卷目录, 可以通过
      `docker volume inspect volume_name` 查看详细信息。
   -  另一种方式是自己指定宿主机的挂载点，在docker-compose中常用写法：
        
      ```yaml
        volumes:
          # 映射到宿主机'/opt/data'目录，根目录路径。
          - /opt/data:/var/lib/mysql
      
          # 以docker-compose.yml文件所在的相对路径。
          - ./cache:/tmp/cache
        
          # 用户目录路径。
          - ~/configs:/etc/configs/:ro
        
          # 命名卷，通过docker创建和管理，在docker的volumes目录下
          - datavolume:/var/lib/mysql
      ```
    
 <br>
 
 #### 使用K8S
 
 ##### kubeadm
 
  - 初始化
    
    ```bash
        kubeadm init --config kubeadm.yaml
    ```
 
 
 
 
 
 
 
 
 
 