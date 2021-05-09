from flask import Flask, render_template, request, redirect, url_for,Blueprint
from pos.models.contactus import Contactus
from pos.models import db

bp = Blueprint("contactus",__name__)


@bp.route("/")
def index():
	return redirect("/contactus")

@bp.route("/contactus")
def contactus_list():
	contactus = Contactus.query.all()
	return render_template("contactus/list.html", contactus=contactus)

@bp.route("/contactus/add", methods=["GET","POST"])
def contactus_add():
	if request.method == "GET":
		return render_template("contactus/form_add.html")
	# ambil data dari form html
	contactus = Contactus()
	# buat contant us utamanya
	contactus.users = request.form.getlist['users']
	contactus.hub = request.form['admin','security']
	contactus.isi = request.form['isi']

 
	db.session.add(contactus)
	# commit semua update yang terjadi 
	db.session.commit()

	return redirect("/contactus")

@bp.route("/contactus/update", methods=["GET","POST"])
def contactus_edit():
	#menentukan nilai apa yang akan diambil jika data diubah
	if request.method == "GET":
		#bikin satu patokan untuk disama ratakan
		con_id = request.args["id"]
		contactus = Contactus.query.filter_by(id=con_id).first()
		return render_template("contactus/form_edit.html", contactus=contactus)
	#bikin satu patokan untuk disama ratakan
	con_id = request.args["id"]
	# melakukan pengupdatean jika ada data didalam berhasil di perbarui
	contactus = contactus.query.filter_by(id=con_id).first()
	contactus.users = request.form.getlist['users']
	contactus.hub = ['admin','security']
	contactus.isi = request.form['isi']

	db.session.add(contactus)
	# commit semua update yang terjadi 
	db.session.commit()
	return redirect("/contactus")

@bp.route("/contactus/delete", methods=["GET"])
def contactus_delete():
	#bikin satu patokan untuk disama ratakan
	con_id = request.args["id"]
	contactus = Contactus.query.filter_by(id=con_id).first()
	#membuat pernyataan jika data berhasil dihapus 
	if contactus:
		db.session.delete(contactus)
		#jika data berhasil dihapus maka data tersebut akan di commit
		db.session.commit()
		return redirect("/contactus")

    