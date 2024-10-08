from flask import Blueprint, request, jsonify
from Entities.Corrida import db, Corrida
from datetime import datetime

corrida_controller = Blueprint('corrida_controller', __name__)


# Adicionar nova corrida
@corrida_controller.route('/add_corrida', methods=['POST'])
def add_corrida():
    data = request.json
    try:
        data_ini = datetime.strptime(data.get('data_ini'), '%Y-%m-%d %H:%M:%S')
        data_fim = datetime.strptime(data.get('data_fim'), '%Y-%m-%d %H:%M:%S')
        end_origem = data.get('end_origem')
        end_fim = data.get('end_fim')
        status = data.get('status')
        id_usuario = data.get('id_usuario')


        new_corrida = Corrida(data_ini=data_ini, data_fim=data_fim, end_origem=end_origem, end_fim=end_fim,
                              status=status,id_usuario=id_usuario)
        db.session.add(new_corrida)
        db.session.commit()

        return jsonify({"message": "Corrida adicionada com sucesso!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Buscar todas as corridas
@corrida_controller.route('/get_corridas', methods=['GET'])
def get_corridas():
    try:
        corridas = Corrida.query.all()
        result = []
        for corrida in corridas:
            corrida_data = {
                'id_corrida': corrida.id_corrida,
                'data_ini': corrida.data_ini.strftime('%Y-%m-%d %H:%M:%S'),
                'data_fim': corrida.data_fim.strftime('%Y-%m-%d %H:%M:%S'),
                'end_origem': corrida.end_origem,
                'end_fim': corrida.end_fim,
                'status': corrida.status,
                'id_usuario' : corrida.id_usuario
            }
            result.append(corrida_data)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Buscar uma corrida específica por ID
@corrida_controller.route('/get_corrida/<string:id>', methods=['GET'])
def get_corrida(id):
    try:
        corridas = Corrida.query.filter_by(id_usuario=id).all()
        if corridas:
            # Create a list of corrida data
            corridas_data = []
            for corrida in corridas:
                corrida_data = {
                    'id_corrida': corrida.id_corrida,
                    'data_ini': corrida.data_ini.strftime('%Y-%m-%d %H:%M:%S'),
                    'data_fim': corrida.data_fim.strftime('%Y-%m-%d %H:%M:%S'),
                    'end_origem': corrida.end_origem,
                    'end_fim': corrida.end_fim,
                    'status': corrida.status
                }
                corridas_data.append(corrida_data)

            return jsonify(corridas_data), 200
        else:
            return jsonify({"message": "Nenhuma corrida encontrada para este usuário"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@corrida_controller.route('/deletar_corrida/<int:id>', methods=['DELETE'])
def deletar_corrida(id):
    try:
        corrida = Corrida.query.get(id)
        if corrida:
            db.session.delete(corrida)
            db.session.commit()
            return '', 204

        else:
            return jsonify({"message": "Corrida não encontrada"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@corrida_controller.route('/update_corrida_origem/<int:id>', methods=["PUT"])
def update_corrida_origem(id):

    try:
        corrida = Corrida.query.get(id)
        if corrida:
            data = request.json
            end_origem = data.get('end_origem')

            corrida.end_origem = end_origem
            db.session.commit()
            return jsonify({"message": "Endereco de origem atualizado com sucesso!"}), 200

        else:
            return jsonify({"message": "Corrida não encontrada"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@corrida_controller.route('/update_corrida_fim/<int:id>', methods=["PUT"])
def update_corrida_fim(id):

    try:
        corrida = Corrida.query.get(id)
        if corrida:
            data = request.json
            end_fim = data.get('end_fim')

            corrida.end_fim = end_fim
            db.session.commit()
            return jsonify({"message": "Endereco de destino atualizado com sucesso!"}), 200

        else:
            return jsonify({"message": "Corrida não encontrada"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 400