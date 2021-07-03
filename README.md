- ZBEAR's Weight Resetter_v_01_08 for Blender(v 2.9x)
- Download .zip or .py and go to bledner -> preferences -> Addons -> Install -> Find downloaded .zip or .py and select it -> OK -> Check the Add-on's check-box searched by keyword like 'zb' or 'wei' -> Use it 

- 🤘 &nbsp;&nbsp; If this add-on was helpful for you, Please Subscribe ZBEAR's Hard Rock YouTube Channel. Let's Rock 
- (☞ﾟヮﾟ)☞ &nbsp;&nbsp;  https://www.youtube.com/channel/UCQF5-PbA0kEV1BLT_pg0KyQ 

<br></br>
< Heavy Metallically Shocked / Weirdly Weighted Result by Some Automatic Weighting Techniques or Hand Weighting Works >

![case1_1](https://user-images.githubusercontent.com/86638301/124344076-5d1f1080-dc0b-11eb-908e-4464733a749f.gif)

< Heavy Metallically Shocked / Weirdly Weighted Result by Some Automatic Weighting Techniques or Hand Weighting Works >



👀
👀
- A good loop phrase in code can change the world.
- A hard rock album can change the world. => ZBEAR Hard Rock Albums on Internet
- 👀 Studying and applying CG graphics for the better Hard Rocking out
- 🌱 python - bpy simple scripting, Add-on development, CG works for Hard Rocking out using Blender
- 👋 ZBEAR, Hard Rock Guitarist, Album Unfinished Fight 1, 2
- 📫 zorzybear@gmail.com, www.zbear.co.kr


🌱 More Details about this add-on: 

A good loop phrase can change the world.
A rock sound with some meaning can change the world.
=> zbear on internet

👋 Guide lines of this tool:

📫 Description Viewpoint A : Public service performance style

The mesh part which is confused by the various cases and operates is registered as the new vertex group and all vertices in the registered vertex group are liberated from all interference by the unknown several bones. This new vertex group's weights will be reset by the weight value given your inputted float value for an additional specified bone. This simplifies the complex situation affected by various bones. This simplifies the indiscriminate weighting of a vertices part caused by automatic weight paint, and helps to keep the work going by making the weighting situation of irregular mesh simple again without backing down from the middle point of the work.

![ZB_RWT](https://user-images.githubusercontent.com/86638301/124344153-c2730180-dc0b-11eb-85e7-2c720a1061da.gif)


- UI No. 0: There must be an active object in selection, and its name must be on UI.
- UI No. 1: Collect the Vertices that have been interfered with and lost their way for all of armature's Bones, designate them as the new Vertex Group and prepare new name for this Group.
- UI No. 2: Enter the name of the new vertex group above.
- UI No. 3: Decide one bone to be attached on your New Vertex Group (if the weighting states of this vertex group are already nice, that vertices in that group's will return to the position of their non-weighted original local location).
- UI No. 4: Enter the name of the bone you picked from above.
- UI No. 5: Enter the weight value to decide how much the Vertex Group will be affected by the Bone entered by you
- UI No. 6: Check all parts and click this button if there is no logical flaw.


![01l_foot_err_01](https://user-images.githubusercontent.com/86638301/124344206-edf5ec00-dc0b-11eb-8388-e36ff57fcc42.jpg)
![02l_foot_relevant_bone_01](https://user-images.githubusercontent.com/86638301/124344208-ee8e8280-dc0b-11eb-8f36-77bf85944179.jpg)
![03l_foot_new_vgroup_reset_01](https://user-images.githubusercontent.com/86638301/124344209-ef271900-dc0b-11eb-8cb0-f284a487c567.jpg)
![04l_foot_src_ctrlcv_01](https://user-images.githubusercontent.com/86638301/124344210-ef271900-dc0b-11eb-869d-337a3060bebe.jpg)
![05l_foot_revelantbonename_copy_01](https://user-images.githubusercontent.com/86638301/124344211-efbfaf80-dc0b-11eb-86c5-2b6c906332ac.jpg)
![07l_foot_decide_weight_for_the_bone_01](https://user-images.githubusercontent.com/86638301/124344212-efbfaf80-dc0b-11eb-8a9c-38d73b900e51.jpg)
![08l_foot_click_big_button_01](https://user-images.githubusercontent.com/86638301/124344214-f0584600-dc0b-11eb-8db8-d2d76e960ee3.jpg)
![09l_foot_last_fixed_01](https://user-images.githubusercontent.com/86638301/124344215-f0584600-dc0b-11eb-8747-f7f9a2a618aa.jpg)



📫 Description Viewpoint B :  Casual style


- This tool can be used at more proper situation through the way of resetting partial weight to 0 and giving weights only to one of the most relevant bones. It would be better than keep your working state in the following situations :

- Specially, in case of the mesh which is skinned with all kinds of the automatic weighting techniques, the weighting result is partly very complicatedly twisted and it shows the undesirable deforming shapes in the pose change

- Use as an assistant tool of weighting solution when it's  needed to correct accidental weighting twisting by various automatic weighting techniques

- When the weights of the vertices blocked from the view were painted weirdly by multiple bones, and even this situation was accumulated, and UNDO function is no more helpful to recover, or you feel like the one more UNDO can shutting down the Blender

- When using weight painting mode and even if you still clicking Ctrl + LMB on each bones for more than 40 minutes but there is no better

- Even doing one more action with Ctrl + Bone clicking is disgustingly tired and mentally painful

⚡⚡ !! Cautions

When certain vertexes do not respond to the addon's operation or pop out :

- Most of the vertex groups that have already been used are able to be reused as a target-group again, but sometimes one or two points can't be processed or mis-handled.

: In that case, through the way that you abandone or reconfigure the used vertex group for resetting a weirdly weighted part of the mesh, most cases related with this problem can be solved.

- The reason of this phenomenon may be the bug of your hand that included some unrelated vertexes when you're in the unconscious, or the bug of certain Automatic Weight Solutions, or the bug from the inside of the blender, or the bug of my code.

- When creating a vertex group to reset, be careful that unrelated vertex is unknowingly included due to unconscious mouse clicks, etc.

: In this case, that one vertex can pop out to the unwanted place after execution. This is because the weight information is initialized together while the vertex is in the group to be reset and the bone you selected has no interesting for this vertex.


- A good loop phrase in code can change the world.
- A hard rock album can change the world. => ZBEAR Hard Rock Albums on Internet
- 👀 Studying and applying CG graphics for the better Hard Rocking out
- 🌱 python - bpy simple scripting, Add-on development, CG works for Hard Rocking out using Blender
- 👋 ZBEAR, Hard Rock Guitarist, Album Unfinished Fight 1, 2
- 📫 zorzybear@gmail.com, 
- 
🌱🌱 If this works was helpful for you, Please Subscribe ZBEAR's YouTube Channel !!: 
🌱🌱 https://www.youtube.com/channel/UCQF5-PbA0kEV1BLT_pg0KyQ
- 
- www.zbear.co.kr



<!---
ZBEAR-Rockn/ZBEAR-Rockn is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
