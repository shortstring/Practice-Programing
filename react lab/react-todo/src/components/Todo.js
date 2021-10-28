import { useState } from 'react';
import Modal from './Modal';
import Backdrop from './Backdrop';
//props is a react concept, js object where all atributes are available as key value pairs in the object.

// any java script expression goes between {}, treated as javascript, any single line, no blocks.. like if statements.
function Todo(props) {
    const [modalIsOpen, setModalIsOpen] = useState(false); //creates a state - returns an array with two elements

    function deleteHandler() {
        setModalIsOpen(true);
    }

    function closeModalHandler() {
        setModalIsOpen(false);
    }

    function closeModalDelete() {
        props.Todo.
        setModalIsOpen(false);
    }
    return ( <
            div className = "card" >
            <
            h2 > { props.text } < /h2> <
            div >
            <
            button id = "btn"
            onClick = { deleteHandler } > Delete < /button> <
            /div> {
                modalIsOpen && < Modal onCancel = { closeModalHandler }
                onConfirm = { closeModalDelete }
                />} {
                    modalIsOpen && < Backdrop onClick = { closeModalHandler }
                    />} <
                    /div>
                );
            }

            //name SHOULD start with a capital letter. (custom elements..)
            export default Todo;