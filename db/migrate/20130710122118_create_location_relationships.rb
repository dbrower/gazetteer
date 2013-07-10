class CreateLocationRelationships < ActiveRecord::Migration
  def change
    create_table :location_relationships, id: false do |t|
      t.integer :parent_location_id, index: true, null: false
      t.integer :child_location_id, index: true, null: false

      t.timestamps
      t.index [:parent_location_id, :child_location_id], unique: true
    end
  end
end
