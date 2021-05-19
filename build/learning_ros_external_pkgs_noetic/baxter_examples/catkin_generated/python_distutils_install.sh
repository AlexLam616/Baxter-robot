#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/alex/workspace/src/learning_ros_external_pkgs_noetic/baxter_examples"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/alex/workspace/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/alex/workspace/install/lib/python3/dist-packages:/home/alex/workspace/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/alex/workspace/build" \
    "/usr/bin/python3" \
    "/home/alex/workspace/src/learning_ros_external_pkgs_noetic/baxter_examples/setup.py" \
     \
    build --build-base "/home/alex/workspace/build/learning_ros_external_pkgs_noetic/baxter_examples" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/alex/workspace/install" --install-scripts="/home/alex/workspace/install/bin"
