function Modal(props) {
    function cancelHandler() {
        props.onCancel();
    }

    function confirmHandler() {
        props.onConfirm();
    }

    return (<div className='modal'>
        <p> Are you Sure</p>
        <button id="btn" onClick = {cancelHandler}>Cancel</button>
        <button id="btn" onClick = {confirmHandler}>Confirm</button>
    </div>
    );
}

export default Modal