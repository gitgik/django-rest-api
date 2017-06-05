pkg_origin=gitgik
pkg_name=django-api
pkg_version=0.1.0
pkg_maintainer="jeegiks@gmail.com"
pkg_upstream_url="https://github.com/gitgik/django-rest-api.git"
pkg_exports=([port]=listening_port)
pkg_exposes=(port)
pkg_build_deps=(core/virtualenv)
pkg_deps=(core/python core/coreutils)
pkg_licence=('MIT')
pkg_interpreters=(bin/python3)

do_verify () {
  return 0
}

do_clean() {
  return 0
}

do_unpack() {
  # copy the contents of the source directory to the habitat cache path
  PROJECT_ROOT="${PLAN_CONTEXT}/.."

  mkdir -p $pkg_prefix
  build_line "Copying project data to $pkg_prefix/"
  cp -r $PROJECT_ROOT/project $pkg_prefix/
  cp -r $PROJECT_ROOT/rest_api $pkg_prefix/
  cp -r $PROJECT_ROOT/*.py $pkg_prefix/
  cp -r $PROJECT_ROOT/requirements.txt $pkg_prefix/
  build_line "Copying .env file with preset variables..."
}

do_build() {
  return 0
}

do_install() {
  cd $pkg_prefix
  build_line "Creating virtual environment..."
  virtualenv venv
  source venv/bin/activate
  pip3 install -r requirements.txt
  build_line "Done installing requirements..."
}
