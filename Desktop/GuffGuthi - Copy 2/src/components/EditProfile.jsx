import "./EditProfile.css"

function EditProfile(){
    return(
        <>
            <section>
                <h1>Edit profile</h1>
                <div>
                    <p>Change profile</p>
                    <img src="./src/assets/profile.jpg" alt="Profile" />
                    <button>Change profile</button>
                </div>
                <div>
                    <form >
                        <div>
                        <label>Change username</label>
                        <br />
                        <input type="text" />
                        <br />
                        <label>Bio</label>
                        <br />
                        <input type="text" />
                        <br />
                        <label>Occupation</label>
                        <br />
                        <input type="text" />
                        <br />
                        <label>Change location</label>
                        <br />
                        <input type="text" />
                        <br />
                        <label> Cover image</label>
                        <button>Change cover</button>
                        </div>
                        <br />
                        <button>Update profile</button>
                    </form>
                </div>
            </section>
        </>
    )
}

export default EditProfile