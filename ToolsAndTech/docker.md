### Docker
> Image --> docker run --> Container <br>

1. ```docker images``` <br>
lists the images

2. ```docker run -it ubuntu:latest bash``` <br>
    bash: the process to be run 

    ubuntu:latest is the name:tag of the image to uniquely identify an image. could also use its ID. 

    ```-it``` stands for terminal interactive. causes the image to have a complete terminal

3. ```docker ps``` <br>
    lists the name of the container

    auto-assigns a cool name to the container as well

    ```-a```: use this option to see <font color="orange">all (including exited)</font> images.

    ```-l```: use this option to see <font color="orange">last exited</font> images.


> When containers exit, they dont get deleted. they are stopped. If you stored some files in a container, you can commit that container back into an image so that when you run the image, it spins a container with the files from earlier.

4. ```docker commit <CONTAINER_ID/NAME>``` <br>
    makes an image out of the container state. results in a big hash.

    run ```docker tag <HASH> my_image_name``` to give the image a name.

    can also run ```docker commit <CONTAINER_ID/NAME> my_image_name``` to avoid doing tag everytime.

> When the main process exits, the container stops. 

5. <font color="cyan">Miscellaneous</font> <br>
    Use `docker run --rm -it ubuntu bash -c "sleep 3; echo all done;"`

    ```docker run --itd ubuntu bash```: opens a container running in background. Later can see that container using ps and enter it by using `docker attach <NAME>`.

    Use <font color="orange">Ctrl+p,Ctrl+q</font> to again detach from that contained but leave it running to attach back later.

    Give your own name by adding `--name` flag.

    Containers can refer to the machine hosting them using `host.docker.internal`.    

    Add -p option to specify port forwarding (bi-directional).

6. ```docker exec``` <br>
    Add another process to a running container. Can't add ports or volumes of fancy stuff with this command though.

    Good for debugging.

7. ```docker logs <CONTAINER_NAME``` <br>
    Logs are around as long as container is around. 

    Dont write huge logs, can crash docker.

8. `docker kill <CONTAINER_NAME>` and `docker rm <CONTAINER_NAME>` <br>
    kill to stop. <br>
    rm to remove.

9. <font color="cyan">Shell and Exec forms</font> <br>

    - Shell Form <br>
    ```<instruction> <command>```    
    e.g. RUN apt-get install python3, CMD echo "Hello World" etc. 
    e.g. 
        ```
            ENV name John Dow
            ENTRYPOINT echo "Hello ${name}"
        ```
        would return <font color="orange">Hello John Doe.</font> upon a docker container run. 
    
    - Exec Form <br>
    ```<instruction> ["executable", "param1", "param2"]``` <br>
    e.g RUN ["apt-get", "install", "python3"], CMD ["/bin/bash", "echo Hello world"] <br>
    e.g 
        ```
            ENV name John Dow
            ENTRYPOINT ["/bin/bash", "-c", "echo Hello, $name"]
        ```
        would return same output as above upon docker container run. 


10. > **RUN** <br>

    Allows to install application and packages reqd for it. Executes any commands on top of current image and creates a sorta layering. by commiting results. Often find multiple of these in a dockerfile. 

11. > **CMD** <br>

    Allows to set a dafault commands which is executed only when container is <font color="orange">run without specifying a command.</font> If Dockerfile has more than one CMD, all but the last are ignored. 

12. > **ENTRYPOINT** <br>

    This is not ignored even when the Docker container runs with command line arguments. 
    ```
        ENTRYPOINT ["/bin/bash", "echo Hello"]
        CMD ["world]
    ```
    when run with ```docker container run -it <image>``` would return **Hello world** but when run with ```docker container run -it <image> John``` would return **Hello John**. 


    





